# mySlidesLive
> ...helps you to extract your SlidesLive presentation.


## Install

```bash
pip install myslideslive
```

## Usage

### Python

In a Python console:

```python
from myslideslive import SlidesLive

msl = SlidesLive('https://slideslive.com/38956531/'
                 'beyond-static-papers-'
                 'rethinking-how-we-share-scientific-understanding-in-ml')
msl.download_slides(slide=(1074, 1075))
msl.compose_video()
```

    
    
    
    Extracted time segment in seconds:
        15215.247--15250.244


### CLI

Directly from terminal:
```bash
msl --slide 1074 1075 \
https://slideslive.com/38956531/beyond-static-papers-rethinking-how-we-share-scientific-understanding-in-ml
```

## Development
- To develop this package you need [nbdev].
- The library is built with `nbdev_build_lib` and `nbdev_update_lib`.
- `nbdev_build_lib` also builds the `Makefile`.
- The `README.md` is regenerated with `nbdev_build_docs`.
- The git hooks are set up with `nbdev_install_git_hooks`.

[nbdev]: https://nbdev.fast.ai/

## What about the SlidesLive video recording?
If you want to get the video recording of your SlidesLive presentation as well,
[youtube-dl] can take care of that.
Then you can cut the video with:
```bash
ffmpeg -ss [start] -i video_in.mp4 -t [duration] -c copy video_out.mp4
```
where `[start]` specifies the start time, e.g. `00:01:23.000` or `83` (in seconds);
and `[duration]` specifies the duration in the same format.
Alternatively to `-t [duration]`, you may use `-to [end]`.

[youtube-dl]: https://github.com/ytdl-org/youtube-dl

## About

This Python module was inspired by:
* <https://github.com/Chandrahasd/slideslive-slides-dl>; and
* <https://github.com/AugustKarlstedt/slideslive-downloader>.
