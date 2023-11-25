# puppet declarative script to install flask from pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

