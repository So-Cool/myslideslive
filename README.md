# mySlidesLive
> ...helps you to extract your SlidesLive presentation.


[![Licence][licence-badge]][licence-link]
[![Python][python-badge]][python-link]
[![PyPI][pypi-badge]][pypi-link]
[![Documentation][doc-badge]][doc-link]

[licence-badge]: https://img.shields.io/github/license/so-cool/myslideslive.svg
[licence-link]: https://github.com/so-cool/myslideslive/blob/master/LICENSE
[python-badge]: https://img.shields.io/badge/python-3.6-blue.svg
[python-link]: https://github.com/so-cool/myslideslive
[pypi-badge]: https://img.shields.io/pypi/v/myslideslive.svg
[pypi-link]: https://pypi.org/project/myslideslive
[doc-badge]: https://img.shields.io/badge/read-documentation-blue.svg
[doc-link]: https://so-cool.github.io/myslideslive

## Install

```bash
pip install myslideslive
```

## Usage

### Python

In a Python console:

```
from myslideslive import SlidesLive

msl = SlidesLive('https://slideslive.com/38956531/'
                 'beyond-static-papers-'
                 'rethinking-how-we-share-scientific-understanding-in-ml')
msl.download_slides(slide=(1074, 1075))
msl.compose_video()
```

### CLI

Directly from terminal:
```bash
msl --slide 1074 1075 \
https://slideslive.com/38956531/beyond-static-papers-rethinking-how-we-share-scientific-understanding-in-ml
```

## Development
- To develop this package you need [nbdev] v1 (`pip install "nbdev<2"`).
- The library (and `Makefile`) is built with `nbdev_build_lib`.
- `nbdev_update_lib` updates the notebooks based on changes in the library.
- The `README.md` is regenerated with `nbdev_build_docs`.
- The git hooks are set up with `nbdev_install_git_hooks`.
- `jupyter nbconvert --clear-output --inplace notebook.ipynb` clears all output cells of a notebook.

Before committing code changes make sure to run:
```bash
nbdev_install_git_hooks && \
nbdev_build_lib && \
nbdev_build_docs && \
nbdev_clean_nbs --clear_all True && \
nbdev_test_nbs
```

[nbdev]: https://nbdev.fast.ai/

## What about the SlidesLive video recording?
If you want to get the video recording of your SlidesLive presentation as well,
[youtube-dl] can take care of that.

## Cutting the video
Then you can cut the video with:
```bash
ffmpeg -i video_in.mp4 -ss [start] -t [duration] -c copy video_out.mp4
```
where `[start]` specifies the start time, e.g. `00:01:23.000` or `83` (in seconds);
and `[duration]` specifies the duration in the same format.
Alternatively to `-t [duration]`, you may use `-to [end]`, i.e.:
```bash
ffmpeg -i video_in.mp4 -ss [start] -to [end] -c copy video_out.mp4
```
**NOTE:** the order of ffmpeg flags seems to influence the precision of
the video cut.

## Picture-in-Picture embedding
To embed the video recording within the bottom-right part of the presentation video,
preserving the audio stream from the former use:
```bash
ffmpeg -i embedded_video.mp4 -i main_video.mp4 \
  -filter_complex "[0] scale=iw/10:ih/10 [embed]; \
                   [1] fps=25 [bg]; \
                   [bg][embed] overlay=main_w-overlay_w:main_h-overlay_h" \
  -framerate 25 \
  -b:v 4810k \
  -b:a 126k \
  -ar 44100 \
  PiP_video.mp4
```
The sound stream is always taken from the first video in the input (`-i`) list;
if you swap the input videos, you also need to swap `[0]` and `[1]` in
the filter string (`-filter_complex`).
To move the embedded video to a different position, you need to change
the `overlay` parameter.
For example, `overlay=main_w-overlay_w:0` will place the embed in
the top-right corner; `overlay=0:0` in the top-left; and
`overlay=0:main_h-overlay_h` in the bottom-left.

[youtube-dl]: https://github.com/ytdl-org/youtube-dl

## About

This Python module was inspired by:
* <https://github.com/Chandrahasd/slideslive-slides-dl>; and
* <https://github.com/AugustKarlstedt/slideslive-downloader>.

PiP ffmpeg command comes from [here](https://www.oodlestechnologies.com/blogs/PICTURE-IN-PICTURE-effect-using-FFMPEG/).
