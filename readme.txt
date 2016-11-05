I took some pictures at the park
I didn't work too much with images at ISS with Marty
I'd like to spend more time with images (lol maybe I can get to soundscapes later)
a responsive image gallery, coded "by hand" (no bootstrap? scary. do it.)

I have full size images. different sizes, different aspect ratios.  
I only want to send the user thumbnails upfront, and upon click fetch( and keep!) the full-size;

steps (at least ones that are clear at this point):
  create thumbnails
  prototype display list of thumbnails
  prototype lightbox popup
  come up with a plan/algorithm to handle thumbnail click and image fetching
  take more pictures ;-)


** on lightbox popup
  responsive?  working on both monitors and phones, landscape and portrait
    using an appropriately sized source image (not just css!) based on device characteristics
    usable!  choose image, see image fill screen, eliminate distraction, but easy to choose other image if desired.
    togglable lightbox, triggered by thumbnails.  flexbox for thumbnails seems to work nicely.

    challenging because images can be any size or aspect ratio, and so can the screen. screen might change aspect ratio midway through usage.

  need to practice more with different image sizes, ratios, and display tactics.  
  lorem pixel can be used, lorempixel.com/width/height urls can be generated "randomly"

what about....thumbnails images whose src is the same as fullsize
  except with prefix.

lightbox gets dynamically generated. at the beginning (sans images)
  there is a slide for every image with a class based on its index or src or something
  when the thumb is clicked, we show the corresponding slide, and look for an img with the right src.  if not there, we put it there (forcing download).
  hide all other slides.  

