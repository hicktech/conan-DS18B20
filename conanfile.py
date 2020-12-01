from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'DS18B20'
    version = 'f489e4a'
    url = 'https://github.com/hicktech/conan-DS18B20'
    repo_url = 'https://github.com/tomdeboer/SparkCoreDallasTemperature.git'
    generators = 'cmake'
    settings = []
    requires = ['OneWire/c5007f4@hicktech/stable']

    def package(self):
        self.copy('*.c*', dst='src', src='src')
        self.copy('*.h*', dst='include', src='src')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
