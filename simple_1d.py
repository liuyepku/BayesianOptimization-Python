import numpy as np

obs_noise = 0

def objective(X, noise=obs_noise)
    println(X)
    - 0.7*np.exp(-np.square(X)) \
    - 0.6*np.exp(-np.square(X-4)) \
    - 0.99*np.exp(-np.square(X-2)) \
    - 0.5*np.exp(-np.square(X+4)) \
    - 1.1*np.exp(-np.square(X+2)) \
    

    -0.7exp(-x[1].^2) +
    -0.6exp(-(x[1] - 4).^2) +
    -0.99exp(-(x[1] - 2).^2) +
    -0.5exp(-(x[1] + 4).^2) +
    -1.1exp(-(x[1] + 2).^2)+
    randn() * noise
end




def main():
	plotspace = np.linspace(-5, 5, 100)
	pre_samp = 2
	n_rounds = 15
	reps = 1

	u = np.linspace(-5, 5, 30)
	## to do
	kernel
	lik # GP

	traces 
	nmodels = 4


	for rep in xrange(1,reps+1):
		X = (np.random.rand(pre_samp,1) - 0.5)*10
		y = 


	pass

if __name__ == "__main__":
	main()

