pip3 install ipyleaflet
git clone https://github.com/ellisonbg/ipyleaflet.git
cd ipyleaflet
sudo pip3 install -e .
jupyter nbextension install --py --symlink --sys-prefix ipyleaflet
jupyter nbextension enable --py --sys-prefix ipyleaflet
