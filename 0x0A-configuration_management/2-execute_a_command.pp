# Manifest that kills 'killmenow' using pkill
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin/killmenow',
  refreshonly => true,
}

