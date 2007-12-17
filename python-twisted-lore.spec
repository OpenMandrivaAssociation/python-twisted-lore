Summary:        A documentation generator
Name:           python-twisted-lore
Version:        0.2.0
Release:        %mkrel 2
Source0:        http://tmrc.mit.edu/mirror/twisted/Lore/0.2/TwistedLore-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/lore/
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


