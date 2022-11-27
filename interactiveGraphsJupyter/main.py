{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1af51db6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "x = np.random.uniform(0, 5, size=100)\n",
    "noise = np.random.normal(size=100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "20a8f142",
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_fct(w=1):\n",
    "   \n",
    "    y = 2 * x + w * noise\n",
    "    plt.scatter(x, y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "31e5480a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dc3d5d7ea41d434590cd8d352f5948a3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(FloatSlider(value=1.0, description='w', max=10.0), Output()), _dom_classes=('widget-inte…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.plot_fct(w=1)>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipywidgets.interact(plot_fct, w=(0, 10, 0.1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d89aa2ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import make_moons\n",
    "\n",
    "def plot_moons(samples=200, noise=0):\n",
    "    moons = make_moons(n_samples=samples, noise=noise)\n",
    "    x, y = moons[0], moons[1]\n",
    "    plt.scatter(x[:, 0], x[:, 1], c=y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5b216312",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e52db9b3ec764a4e89059c71a2918570",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(Dropdown(description='samples', options=(200, 500, 1000), value=200), FloatSlider(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.plot_moons(samples=200, noise=0)>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipywidgets.interact(plot_moons, samples=[200, 500, 1000], noise=(0, 2, 0.025))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f25d58e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_sin(start=0, end=30, factor=1, grid=True, plot_cos=False):\n",
    "    x = np.linspace(start, end, (end - start) * 10)\n",
    "    y = np.sin(x) * factor\n",
    "    plt.grid(grid)\n",
    "    plt.plot(x,y)\n",
    "    if plot_cos:\n",
    "        y = np.cos(x)\n",
    "        plt.plot(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "9d5291fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d5d49845ddcb4df494d717e41d122ef5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(IntSlider(value=0, description='start', max=10), IntSlider(value=30, description='end', …"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.plot_sin(start=0, end=30, factor=1, grid=True, plot_cos=False)>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipywidgets.interact(plot_sin, start=(0, 10, 1), end=(20, 50, 1), factor=(0, 5, 0.1), grid=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f3a5eb7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
