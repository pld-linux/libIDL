%define glib_version 1.3.12.90

Summary: Library for parsing IDL (Interface Definition Language)
Name: libIDL
Version: 0.7.1.91
Release: 1
Source: ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/libIDL/%{name}-%{version}.tar.gz
Group: System Environment/Libraries
License: LGPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: pkgconfig >= 0.8
BuildRequires: glib2-devel >= %{glib_version}


%description

libIDL is a library for parsing IDL (Interface Definition Language). 
It can be used for both COM-style and CORBA-style IDL.

%package devel
Summary: Development libraries and header files for libIDL
Group: Development/Libraries
Requires: libIDL = %{version}
Requires: pkgconfig >= 0.8
Requires: glib2-devel >= %{glib_version}

%description devel


libIDL is a library for parsing IDL (Interface Definition Language). 
It can be used for both COM-style and CORBA-style IDL.

This package contains the header files and libraries needed to write 
or compile programs that use libIDL.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

gzip -9 %{buildroot}%{_infodir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/libIDL2.info.gz %{_infodir}/dir

%preun devel
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/libIDL2.info.gz %{_infodir}/dir
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%{_includedir}/*
%{_libdir}/lib*.so.*

%doc AUTHORS COPYING README NEWS

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*
%{_bindir}/libIDL-config-2
%{_infodir}/libIDL2.info.gz

%changelog
* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- cvs snap 0.7.1.91

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- cvs snap, rebuild on new glib 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- glib 1.3.10

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- initial build of standalone libIDL
- fix braindamage
