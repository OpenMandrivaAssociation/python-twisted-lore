%define name python-twisted-lore
%define version 12.2.0
%define rel 1
%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

Summary:        A documentation generator
Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
Source0:        http://tmrc.mit.edu/mirror/twisted/Lore/%{mainver}/TwistedLore-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedLore
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# for docbook, lmath, etc
Requires:       python-twisted-web

%description
Twisted Lore is the documentation generator of the Twisted matrix
framework.

%prep
%setup -q -n TwistedLore-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1

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
