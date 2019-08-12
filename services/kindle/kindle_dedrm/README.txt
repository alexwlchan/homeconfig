Vendored version of https://github.com/ch33s3w0rm/kindle_dedrm

Taken at commit 7773a22

====

kindle_dedrm: Python 2.x script for removing DRM from Kindle and .prc e-books

To use, install Python 2.x (recommended: 2.7, 2.6 or 2.5), download the
kindle_dedrm script from here:
https://github.com/ch33s3w0rm/kindle_dedrm/raw/master/release/kindle_dedrm
, and run it in the command-line. There is no graphical user interface.

Compatible with Linux, Mac OS X, Windows and any operating system Python 2.x
runs on.

For maximum speed, use Python 2.7, 2.6, 2.5 or 2.4 (the latter with the
ctypes extension installed) on Linux, Mac OS X or Windows, on i386 (x86) or
amd64 (x86_64). You also get maximum speed with Python 2.4 on Linux i386,
because the dl module is used.

To use it with Python 2.5 or 2.4 or Windows, you have to unzip the
kindle_dedrm script first.

Based on tools_v5.3.1 by Apprentice Alf:
http://apprenticealf.wordpress.com/2012/09/10/drm-removal-tools-for-ebooks/

FAQ
~~~
Q1. Why not use the K4MobiDeDRM Calibre plugin (part of the tools archive
    http://apprenticealf.wordpress.com/2012/09/10/drm-removal-tools-for-ebooks/
    ) instead?

A1. Use that if you like it. The most important differences are:
    kindle_dedrm is a command-line tool supporting fully automated batch
    operation, and it has much fewer dependencies than K4MobiDeDRM, i.e. it
    can run on systems to which it is not feasible to install Calibre.

__EOF__
