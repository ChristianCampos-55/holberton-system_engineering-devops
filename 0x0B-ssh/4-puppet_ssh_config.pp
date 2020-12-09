#SSH config with puppet
file { '/etc/ssh/ssh_config':
  path	  => 'file',
  line	  => '	IdentityFile ~/.ssh/holberton',
  replace =>true,
}

file { '/etc/ssh/ssh_config':
  path	  => 'file',
  line	  => '	PasswordAuthentication no',
  replace =>true,
}
