#SSH config with puppet
file { '/etc/ssh/ssh_config':
  path	  => 'file',
  line	  => '	IdentityFile ~/.ssh/holberton',
  replace =>true,
}
