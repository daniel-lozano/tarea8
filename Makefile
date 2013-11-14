all: graficas

graficas:ctes.ipynb

	ipython notebook ctes.ipynb &
clean:
	rm -f	*.png