import os
import re
import yaml
from typing import Any, Dict, List

# Needed to parse !!python/name:material.extensions.emoji.twemoji
import material.extensions.emoji

# Needed to parse !!python/name:pymdownx.superfences.fence_code_format
import pymdownx.superfences


def load_yaml_with_env_variables(file_path: str) -> Dict[str, Any]:
    """
    Load a YAML file while resolving environment variables defined using !ENV ${VAR_NAME}.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed YAML content with environment variables replaced.
    """
    tag = "!ENV"
    pattern = re.compile(r".*?\${([A-Z0-9_]+)}.*?")

    def constructor_env_variables(loader, node):
        """Replace !ENV ${VAR_NAME} with the actual environment variable values."""
        value = loader.construct_scalar(node)
        for var in pattern.findall(value):
            value = value.replace(f"${{{var}}}", os.environ.get(var, var))
        return value

    loader = yaml.FullLoader
    loader.add_implicit_resolver(tag, pattern, None)
    loader.add_constructor(tag, constructor_env_variables)

    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.full_load(file)


def merge_yaml(base_config: Dict[str, Any], override_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively merges two YAML dictionaries. The override_config values replace or extend base_config.

    Args:
        base_config (dict): The base YAML configuration.
        override_config (dict): The YAML configuration that overrides the base.

    Returns:
        dict: The merged YAML configuration.
    """
    if not isinstance(base_config, dict):
        return override_config

    merged_config = base_config.copy()

    for key, override_value in override_config.items():
        if key in merged_config:
            base_value = merged_config[key]
            if isinstance(base_value, dict) and isinstance(override_value, dict):
                merged_config[key] = merge_yaml(base_value, override_value)
            elif isinstance(base_value, list) and isinstance(override_value, list):
                merged_config[key] = merge_lists(base_value, override_value)
            else:
                merged_config[key] = override_value
        else:
            merged_config[key] = override_value

    return merged_config


def merge_lists(base_list: List[Any], override_list: List[Any]) -> List[Any]:
    """
    Merges two lists while ensuring dictionaries with the same key are merged
    and other values are appended without duplication.

    - If an item in the list is a dictionary with a single key, and a matching dictionary exists,
      they are merged instead of duplicated.
    - Other values are added uniquely.

    Args:
        base_list (list): The base list.
        override_list (list): The overriding list.

    Returns:
        list: The merged list.
    """
    merged_list = []
    seen_items = {}

    for item in base_list + override_list:
        if isinstance(item, dict) and len(item) == 1:
            key = next(iter(item))  # Extract dictionary key (e.g., "mkdocs-jupyter")
            if key in seen_items:
                seen_items[key] = merge_yaml(seen_items[key], item[key])  # Merge dictionaries
            else:
                seen_items[key] = item[key]
        elif item not in merged_list:
            merged_list.append(item)

    # Convert merged dictionary values back into list format
    for key, value in seen_items.items():
        merged_list.append({key: value})

    return merged_list


def save_yaml(data: Dict[str, Any], output_file: str) -> None:
    """
    Save a YAML dictionary to a file, ensuring proper Unicode handling and preserving !!python/name tags.

    Args:
        data (dict): YAML data to be saved.
        output_file (str): Output file path.
    """

    class CustomDumper(yaml.Dumper):
        """Custom YAML dumper to prevent adding empty quotes for !!python/name."""

        def ignore_aliases(self, data):
            return True  # Prevents unnecessary YAML processing on certain tags

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# WARNING: This file is auto-generated during the build process.\n")
        f.write("# DO NOT EDIT THIS FILE MANUALLY.\n")
        f.write("# It is created by merging:\n")
        f.write("#   - Generic YAML file: ../assets-docs/mkdocs.yml\n")
        f.write("#   - Project specific YAML file: docs/mkdocs.yml\n\n")

    with open(output_file, "a", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            Dumper=CustomDumper,  # Use custom dumper
            allow_unicode=True,  # Ensure Unicode characters like © are preserved
            default_flow_style=False,  #
            sort_keys=False, # Preserve the order of keys
        )


def main() -> None:
    """
    Main function to read, merge, and save YAML configurations.
    """
    generic_config_path = "../assets-docs/mkdocs.yml"
    specific_config_path = "docs/mkdocs.yml"
    output_path = "mkdocs.yml"

    print(f"Reading generic config: {generic_config_path}")
    base_config = load_yaml_with_env_variables(generic_config_path)

    print(f"Reading project specific config: {specific_config_path}")
    override_config = load_yaml_with_env_variables(specific_config_path)

    print(f"Saving merged config: {output_path}")
    merged_config = merge_yaml(base_config, override_config)
    save_yaml(merged_config, output_path)


if __name__ == "__main__":
    main()
