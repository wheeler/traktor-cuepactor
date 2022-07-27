# Traktor Cuepactor
Tools to tidy up your Traktor Pro collection hotcues

## What?

This tool is to improve my personal Traktor workflow by solving some problems with hotcues that are not easy to fix in Traktor Pro.
I use many hotcues in tracks, mostly to make notes of the song structure. The most annoying thing to do when working with hotcues is to need to switch them, because there is no easy way, especially if you name your cuepoints.

### Order hotcues by time
example: `[1 3 2 _ _ _ _ _]` → `[1 2 3 _ _ _ _ _]`

Traktor hotcues can be placed in any order within in a track. I would like to always have them ordered by when they occur in the track. This tool re-orders hotcues to be in order based on time. (For some there may be performance reasons for having hotcues not in order.)

Duplicate hotcues will be ordered by type: `Grid, Load, FadeIn, Cue, FadeOut, Loop`

### Compact hotcues (remove gaps)
example: `[1 _ 3 4 _ _ _ _]` → `[1 2 3 _ _ _ _ _]`

Numbered hotcues can be unused. In the UI this causes an inconsistency: the cues have their true number but if you click the hotcue description dropdown they are "compact" numbered. This inconsistency is confusing to me as I often read hotcue descriptions.
   
### Combined 
Using the combination of these means you can add hotcues to a track without worrying about having them be in order or how many
you cues you are going to use

### Future Plans
- "Snap" existing hot cues
  
  If you create your hotcues for a track and then adjust the grid hotcue your hotcues will not be "snapped" to the grid anymore. If you are using quantize mode I don't think this actually matters but it bothers me a bit. The idea is to make a tool that will adjust the hotcue locations to be "snapped" based on the current grid declaration. If you intentionally do not use quantize in order to use off-grid cues for one-shots this would be bad for you.

## Installation

(July 2022) this requires a fork of `traktor-nml-utils` that has been updated to parse current collection nml files with features like smartlists
```shell
pip install git+https://github.com/b1kjsh/traktor-nml-utils.git@b1kjsh/fixing_smartlists_and_indexing
```
