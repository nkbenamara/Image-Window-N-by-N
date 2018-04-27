def image_window(image,idx,idy,n_kernel):
    """
    A function that brings pixel gray intensities around a central pixel according to a window n by n
    idx and idy are coordinates of a central pixel in an image
    n_kernel is the dimension of the window
    """
    n=int(n_kernel/2)
    window=[]
    for i in range (-n,n+1):
        for j in range (-n,n+1):
            try :
                window.append(image[idx+i,idy+j])
            except:
                window.append(0)
    return window