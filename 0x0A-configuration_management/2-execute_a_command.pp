# Manifest that kills a process named killmenow using pkill
exec { 'kill an infinite loop process':
  command => '/usr/bin/pkill --exact killmenow'
}
