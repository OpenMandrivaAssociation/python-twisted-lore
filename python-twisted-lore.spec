%define version 8.1.0
%define rel 2

Summary:        A documentation generator
Name:           python-twisted-lore
Version:        %version
Release:        %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/Lore/8.1/TwistedLore-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedLore
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
#BuildArch:      noarch
Requires:       python-twisted-core
# for docbook, lmath, etc
Requires:       python-twisted-web

%description
Twisted Lore is the documentation generator of the Twisted matrix
framework.
%prep
%setup -q -n TwistedLore-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir 

%__install -d                      %buildroot%_mandir/man1
%__install -m 644 doc/man/*.1      %buildroot%_mandir/man1

%clean
%__rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%dir %py_platsitedir/twisted/lore
%py_platsitedir/twisted/lore/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
%_mandir/man1/*


