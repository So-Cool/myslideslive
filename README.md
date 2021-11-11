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


    ffmpeg version 4.4 Copyright (c) 2000-2021 the FFmpeg developers
      built with Apple clang version 12.0.0 (clang-1200.0.32.29)
      configuration: --prefix=/usr/local/Cellar/ffmpeg/4.4_2 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags= --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libbluray --enable-libdav1d --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-avresample --enable-videotoolbox
      libavutil      56. 70.100 / 56. 70.100
      libavcodec     58.134.100 / 58.134.100
      libavformat    58. 76.100 / 58. 76.100
      libavdevice    58. 13.100 / 58. 13.100
      libavfilter     7.110.100 /  7.110.100
      libavresample   4.  0.  0 /  4.  0.  0
      libswscale      5.  9.100 /  5.  9.100
      libswresample   3.  9.100 /  3.  9.100
      libpostproc    55.  9.100 / 55.  9.100
    Input #0, concat, from '/var/folders/d0/9mvcgn8503s6975cz1p09rmc0000gn/T/tmpp412iy47':
      Duration: N/A, start: 0.000000, bitrate: N/A
      Stream #0:0: Video: mjpeg (Baseline), yuvj420p(pc, bt470bg/unknown/unknown), 1024x576 [SAR 96:96 DAR 16:9], 25 fps, 25 tbr, 25 tbn, 25 tbc
    Stream mapping:
      Stream #0:0 -> #0:0 (mjpeg (native) -> h264 (libx264))
    Press [q] to stop, [?] for help
    [libx264 @ 0x7fefb100bc00] using SAR=1/1
    [libx264 @ 0x7fefb100bc00] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
    [libx264 @ 0x7fefb100bc00] profile High, level 3.1, 4:2:0, 8-bit
    [libx264 @ 0x7fefb100bc00] 264 - core 163 r3060 5db6aa6 - H.264/MPEG-4 AVC codec - Copyleft 2003-2021 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=6 lookahead_threads=1 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
    Output #0, mp4, to '38956531.mp4':
      Metadata:
        encoder         : Lavf58.76.100
      Stream #0:0: Video: h264 (avc1 / 0x31637661), yuvj420p(pc, bt470bg/unknown/unknown, progressive), 1024x576 [SAR 96:96 DAR 16:9], q=2-31, 25 fps, 12800 tbn
        Metadata:
          encoder         : Lavc58.134.100 libx264
        Side data:
          cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
    frame=    3 fps=0.0 q=-1.0 Lsize=      51kB time=00:00:00.00 bitrate=5316205.1kbits/s speed=0.00172x    
    video:50kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 1.797007%
    [libx264 @ 0x7fefb100bc00] frame I:2     Avg QP: 6.33  size: 25066
    [libx264 @ 0x7fefb100bc00] frame P:1     Avg QP:19.11  size:    98
    [libx264 @ 0x7fefb100bc00] mb I  I16..4: 72.9% 18.7%  8.4%
    [libx264 @ 0x7fefb100bc00] mb P  I16..4:  0.0%  0.0%  0.0%  P16..4:  1.0%  0.0%  0.0%  0.0%  0.0%    skip:99.0%
    [libx264 @ 0x7fefb100bc00] 8x8 transform intra:18.7% inter:0.0%
    [libx264 @ 0x7fefb100bc00] coded y,uvDC,uvAC intra: 18.0% 24.3% 15.4% inter: 0.0% 0.9% 0.0%
    [libx264 @ 0x7fefb100bc00] i16 v,h,dc,p: 88%  8%  4%  0%
    [libx264 @ 0x7fefb100bc00] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 32% 27% 20%  5%  3%  2%  4%  3%  4%
    [libx264 @ 0x7fefb100bc00] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 35% 26% 14%  4%  5%  5%  5%  3%  4%
    [libx264 @ 0x7fefb100bc00] i8c dc,h,v,p: 68% 16% 14%  2%
    [libx264 @ 0x7fefb100bc00] Weighted P-Frames: Y:0.0% UV:0.0%
    [libx264 @ 0x7fefb100bc00] kb/s:9.13


### CLI

Directly from terminal:
```bash
msl --slide 1074 1075 \
https://slideslive.com/38956531/beyond-static-papers-rethinking-how-we-share-scientific-understanding-in-ml
```

## Development
- To develop this package you need [nbdev].
- The library (and `Makefile`) is built with `nbdev_build_lib`.
- `nbdev_update_lib` updates the notebooks based on changes in the library.
- The `README.md` is regenerated with `nbdev_build_docs`.
- The git hooks are set up with `nbdev_install_git_hooks`.

Before commiting code changes make sure to run:
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
