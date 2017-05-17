# bltools
This simple Python scripts can download all or a range of pages of a manuscript from British Library's website. 
BL allows you to view manuscripts on its website but there is no download feature and if you need to study a manuscript carefully, you'll find the website quite frustrating.
Dezoomify by "Ophir LOJKINE" (https://github.com/lovasoa/dezoomify) is also a great tool to download single pages from BL and some other online resources but I needed a simple and straightforward tool to get a manuscript name and download all pages

# Installation

To run the script you'd need python3.x and following libraries:

* Pillow
* requests
* PyYAML
* xmltodict

Normally installing them is as easy as running:
```
pip install module\_name
```

# Download a manuscript

Check the manuscript ID in the British Library website. Each digitised manuscript has a "Display page" with information about it. The URL to this page is something like: [http://www.bl.uk/manuscripts/FullDisplay.aspx?ref=Add_MS_19352](http://www.bl.uk/manuscripts/FullDisplay.aspx?ref=Add_MS_19352). The ID we need is the part after ref=, in this case add\_ms\_19352 (case doesn't matter).

To get this manuscript just edit the config file, set the page range you want to download and run:
```
python directdl.py add_ms_19352
```

# TODO

* Auto discover next page to download (have a downloand all option)
* Use alternative faster web download method
* Generate a report at the end
