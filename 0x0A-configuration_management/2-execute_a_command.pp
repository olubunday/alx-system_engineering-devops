# Manifest that kills 'killmenow' using pkill
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/bin', # Update with the correct path if needed
  refreshonly => true,
  subscribe   => File['/path/to/trigger_file'], # Replace with an actual file triggering the execution
}

