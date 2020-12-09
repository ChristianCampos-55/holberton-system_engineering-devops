#SSH config with puppet
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  path	  => '/etc/ssh/ssh_config',
  line	  => '	IdentityFile ~/.ssh/holberton',
  replace =>true,
}

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  path	  => '/etc/ssh/ssh_config',
  line	  => '	PasswordAuthentication no',
  replace =>true,
}
