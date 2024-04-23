# install puppet-lint -v 2.5.0

exec { 'puppet-lint':
    ciommand => '/usr/bin/apt-get -y install puppet-lint -v 2.1.0',
}
