import Image

image = Image.open('tomato.png')
bw_image = Image.open('tomato-bw.png')

width,height = image.size
original_pixels = list(image.getdata())
num_pixels = len(original_pixels)
num_slices = 40 
fade_slices = 2 
slice_height = float(height)/num_slices
print 'slice height is', slice_height



for slice_num in range(num_slices+1):
    slice_start = int(slice_num*slice_height)
    fade_start = max(slice_start - fade_slices,0)
    num_faded_pixels =  width*(slice_start-fade_start)
    num_sliced_pixels =  width*(slice_start) - num_faded_pixels
    print 'slice %d has start %d, fade_length %d, %d pixels blanked' % (slice_num, slice_start, num_faded_pixels, num_sliced_pixels)
    new_pixels = [ (0,0,0,0) ]*num_sliced_pixels 
    faded_pixels = []
    for faded_num in range(num_faded_pixels) :
        r,g,b,a = original_pixels[num_sliced_pixels+faded_num]
        if not a:
            faded_pixels.append((0,0,0,0))
        else:
            faded_amount = int(255*(float(faded_num)/num_faded_pixels))
            faded_pixels.append((r,g,b,faded_amount))
        
    new_pixels = new_pixels + faded_pixels + original_pixels[num_sliced_pixels+num_faded_pixels:] 
    image.putdata(new_pixels)
    slice_image = bw_image.copy()
    slice_image.paste(image,(0,0),image)
    slice_image.save("tomato-%d.png" % slice_num)

    
