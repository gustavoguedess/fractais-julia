#%%
import numpy as np 
import matplotlib.pyplot as plt

def mandelbrot(n_rows, n_columns, iterations, cx, cy):
    x_cor = np.linspace(-2, 2, n_rows)
    y_cor = np.linspace(-2, 2, n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    c = complex(cx, cy)
    for i in range(x_len):
        for j in range(y_len):
            z = complex(x_cor[i], y_cor[j])
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
        print(int((i/x_len)*100),"% completed")

    print(output)
    plt.imshow(output.T, cmap='hot')
    plt.axis("off")
    plt.show()


#%% Julia #1
mandelbrot(800,600,120,-0.70176,-0.3842)

#%% Julia #2
mandelbrot(800,600,120,0.45,0.1428)

#%% Julia #3
mandelbrot(800,600,120,-0.42,0.6)