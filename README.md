# cura-dremel-3d45-plugin
This is an open source effort to work with the dremel 3d45 over a network/wifi connection with recent Cura versions.

May 2021 - Hello, last year I worked on a private project, so I could use my Dremel 3d45 printer with a more modern slicer than the one that is supplied by the manufacturer. 
I don't want to take all the credit for this plugin. I used stuff from numerous websites and other github projects to get this to the current state.

Be reminded that using the software available on this site is completely on your own risk, and that it is in a beta version state currently. 

I will provide detailed installation instructions shortly, so it becomes easier for people to use this plugin. Personally I find it very frustrating that a lot of github projects are like 'here's a bunch of code, just discover for yourself how to get it to work'.

In the current version, the ipaddress of the printer must be hardcoded into the plugin code. I aim to change that, so that it can be set from a menu, or maybe even with auto-discovering the printer.

Feature wish list:
- monitoring the printer from the Cura monitoring tab
- monitoring by camera, temperature, estimated remaining time, progress percentage
- preferences menu, for ip-address or multiple
- include proven working settings for materials, that can be bought again and again in the same quality. So the manufacturer and the exact type(number) must be known and one or more websites/stores where it can be bought. The aim of this is that we can spend less time adjusting settings and be more creative.
