# Aseprite-Slice-Import
Takes the exported data file from Aseprite's --sheet --data output and translates it to an XML .aseprite-data file for Aseprite to auto-import slice information from.

---

## Dependencies

* python3

---

## Command Line Interface Help

Running `python asepritedata.py -h` will pull up a brief description of the command line inputs, like so:

```
usage: asepritedata.py [-h] [-f] [-jh | -ja] data output

Translate Aseprite's JSON data export from --sheet to XML Slices

positional arguments:
  data          the json data file from aseprite
  output        the corresponding image file name

optional arguments:
  -h, --help    show this help message and exit
  -f, --force   Ignore existing files and overwrite without prompt
  -jh, --hash   Force reading JSON file as a Hash format (default)
  -ja, --array  Force reading JSON file as an Array format
```

---

## How to use it:
Given any number of sprites, import them into an aseprite file with the CLI:

`aseprite.exe -b *.png --sheet-pack --sheet atlas-bestfit.png --data atlas-bestfit.json`

Run the script:

`python asepritedata.py atlas-bestfit.json atlas-bestfit`

Open atlas-bestfit.aseprite and the fiel should be sliced, saving the file will import the slice data to the internal file structure.

## Example usage:

Given any number of sprites, import them into an aseprite file with the CLI:

`aseprite.exe -b *.png --sheet-pack --sheet atlas-bestfit.png --data atlas-bestfit.json`

Opening the .aseprite file shows none of the images were imported as slices:

![Export from Aseprite](https://github.com/FriedYeti/Aseprite-Slice-Import/blob/master/images/AsepriteExport.PNG)

But opening the .json file shows that all of the info is there:

```
atlas-bestfit.json:

{ "frames": {
   "sprite-01.png": {
    "frame": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "rotated": false,
    "trimmed": false,
    "spriteSourceSize": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "sourceSize": { "w": 16, "h": 16 },
    "duration": 100
   },
   "sprite-02.png": {
    "frame": { "x": 16, "y": 0, "w": 16, "h": 16 },
    "rotated": false,
    "trimmed": false,
    "spriteSourceSize": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "sourceSize": { "w": 16, "h": 16 },
    "duration": 100
   },
   "sprite-03.png": {
    "frame": { "x": 32, "y": 0, "w": 16, "h": 16 },
    "rotated": false,
    "trimmed": false,
    "spriteSourceSize": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "sourceSize": { "w": 16, "h": 16 },
    "duration": 100
   },
   "sprite-04.png": {
    "frame": { "x": 48, "y": 0, "w": 16, "h": 16 },
    "rotated": false,
    "trimmed": false,
    "spriteSourceSize": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "sourceSize": { "w": 16, "h": 16 },
    "duration": 100
   },
   "sprite-05.png": {
    "frame": { "x": 0, "y": 16, "w": 16, "h": 16 },
    "rotated": false,
    "trimmed": false,
    "spriteSourceSize": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "sourceSize": { "w": 16, "h": 16 },
    "duration": 100
   },
   "sprite-06.png": {
    "frame": { "x": 16, "y": 16, "w": 16, "h": 16 },
    "rotated": false,
    "trimmed": false,
    "spriteSourceSize": { "x": 0, "y": 0, "w": 16, "h": 16 },
    "sourceSize": { "w": 16, "h": 16 },
    "duration": 100
   }
 },
 "meta": {
  "app": "http://www.aseprite.org/",
  "version": "1.2.9-x64",
  "image": "atlas-bestfit.aseprite",
  "format": "RGBA8888",
  "size": { "w": 64, "h": 32 },
  "scale": "1"
 }
}
```

Running the script:

`python asepritedata.py atlas-bestfit.json atlas-bestfit`

Produces a .aseprite-data file with XML data:

```
atlas-bestfit.aseprite-data:

<?xml version="1.0" encoding="utf-8" ?>
<sprite>
	<slices>
		<slice id="sprite-01" color="#0000ff">
			<key frame="0" x="0" y="0" w="16" h="16" />
		</slice>
		<slice id="sprite-02" color="#0000ff">
			<key frame="0" x="16" y="0" w="16" h="16" />
		</slice>
		<slice id="sprite-03" color="#0000ff">
			<key frame="0" x="32" y="0" w="16" h="16" />
		</slice>
		<slice id="sprite-04" color="#0000ff">
			<key frame="0" x="48" y="0" w="16" h="16" />
		</slice>
		<slice id="sprite-05" color="#0000ff">
			<key frame="0" x="0" y="16" w="16" h="16" />
		</slice>
		<slice id="sprite-06" color="#0000ff">
			<key frame="0" x="16" y="16" w="16" h="16" />
		</slice>
	</slices>
</sprite>
```

Opening the .aseprite file at this point will force Aseprite to read the slice data and import it:

![Aseprite with Slice Data](https://github.com/FriedYeti/Aseprite-Slice-Import/blob/master/images/SlicesImported.PNG)

Saving the .aseprite file at this point will force Aseprite to save all of the slice info into it's internal file structure, allowing you to get rid of the .aseprite-data file.
