# installing a package using puppet
package { 'flask':
  ensure   => '.1.0',
  provider => 'ip3',
}
