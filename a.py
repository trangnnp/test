import gdown

# unmodified train set
url = 'https://drive.google.com/uc?id=1BsikaZTAmoDWKuDqo4MucOq4xo1og_dz&export=download'
output = '/content/dataset/unmodified_train.dat.npy'
gdown.download(url, output, quiet=False)

# unmodified valid set
url = 'https://drive.google.com/uc?id=1pdJLF41StMYPXr02rI8VOl_CUrUVTQJj&export=download'
output = '/content/dataset/unmodified_valid.dat.npy'
gdown.download(url, output, quiet=False)

# unmodified valid set with intervention
url = 'https://drive.google.com/uc?id=1cqRDKgLHvXyG2rHp3W7wwmvqF3Mui9yQ&export=download'
output = '/content/dataset/unmodified_valid_intervention.dat.npy'
gdown.download(url, output, quiet=False)

# # over_sampled train set
# url = 'https://drive.google.com/uc?id=1HuPUqieA6LHxA5CfbrMH8GVnLjvIpB38&export=download'
# output = '/content/dataset/over_sampled_train.dat.npy'
# gdown.download(url, output, quiet=False)

# # under_sampled train set
# url = 'https://drive.google.com/uc?id=1CeEJSSGz0ms9AOa20UQoxUfnfaCpHlHz&export=download'
# output = '/content/dataset/under_sampled_train.dat.npy'
# gdown.download(url, output, quiet=False)

