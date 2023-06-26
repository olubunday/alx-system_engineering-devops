# add configuration lines to simplify connecting to the user server
file_line { 'disable SSH password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^#?\s*PasswordAuthentication\s+\S+$'
}

file_line { 'use school SSH key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^(    |\t)IdentityFile ~/\.ssh/school$'
}

