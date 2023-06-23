# Manifest that kills 'killmenow' using pkill
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin/bash:/bash',
  refreshonly => true,
  subscribe   => File['/Stage[main]/Main/Exec[killmenow]/returns'],
}

