# bltools
This simple Python scripts can download all or a range of pages of a manuscript from British Library's website. 
BL allows you to view manuscripts on its website but there is no download feature and if you need to study a manuscript carefully, you'll find the website quite frustrating.
Dezoomify by "Ophir LOJKINE" (https://github.com/lovasoa/dezoomify) is also a great tool to download single pages from BL and some other online resources but I needed a simple and straightforward tool to get a manuscript name and download all pages

To run the script you'd need python3.x and following libraries:

* Pillow
* requests
* PyYAML
* xmltodict

# TODO

* Auto discover next page to download (have a downloand all option)
* Use alternative faster web download method
* Generate a report at the end
