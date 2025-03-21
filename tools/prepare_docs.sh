echo "\033[0;33m:::::: Add the extra files from the ../assets-docs\033[0m"
cp -R ../assets-docs/docs/assets/ docs/assets/
cp -R ../assets-docs/includes/ includes/
cp -R ../assets-docs/overrides/ overrides/

echo "\033[0;33m:::::: Add the extra files from the ../assets-branding\033[0m"
mkdir -p docs/assets/images/
cp ../assets-branding/easypeasy/hero/dark.png docs/assets/images/hero_dark.png
cp ../assets-branding/easypeasy/hero/light.png docs/assets/images/hero_light.png
cp ../assets-branding/easypeasy/logos/dark.svg docs/assets/images/logo_dark.svg
cp ../assets-branding/easypeasy/logos/light.svg docs/assets/images/logo_light.svg
cp ../assets-branding/easypeasy/icons/color.png docs/assets/images/favicon.png
mkdir -p overrides/.icons/
cp ../assets-branding/easypeasy/icons/bw.svg overrides/.icons/easypeasy.svg
cp ../assets-branding/easyscience-org/icons/eso-icon_bw.svg overrides/.icons/easyscience.svg

echo "\033[0;33m:::::: Add Jupyter notebooks from the project to the docs/\033[0m"
cp -R tutorials/ docs/tutorials/

echo "\033[0;33m:::::: Create the mkdocs.yml configuration file\033[0m"
python tools/create_mkdocs-yml.py
