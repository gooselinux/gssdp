Name:           gssdp
Version:        0.7.1
Release:        1%{?dist}
Summary:        Resource discovery and announcement over SSDP

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://www.gupnp.org/sources/gssdp/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: pkgconfig
BuildRequires: libsoup-devel >= 2.4
BuildRequires: dbus-glib-devel
BuildRequires: glib2-devel >= 2.18
BuildRequires: libxml2-devel
BuildRequires: GConf2-devel
BuildRequires: gtk2-devel
BuildRequires: gtk-doc
BuildRequires: NetworkManager-devel

Requires: dbus

%description
GSSDP implements resource discovery and announcement over SSDP and is part 
of gUPnP.  GUPnP is an object-oriented open source framework for creating 
UPnP devices and control points, written in C using GObject and libsoup. The 
GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development package for gssdp
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libsoup-devel >= 2.4
Requires: glib2-devel >= 2.18
Requires: pkgconfig

%description devel
Files for development with gssdp.

%package docs
Summary: Documentation files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtk-doc
BuildArch: noarch

%description docs
This package contains developer documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS
%dir %{_datadir}/gssdp
%{_bindir}/gssdp-device-sniffer
%{_libdir}/libgssdp-1.0.so.*
%{_datadir}/gssdp/gssdp-device-sniffer.ui

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgssdp-1.0.so
%{_libdir}/pkgconfig/gssdp-1.0.pc
%{_includedir}/gssdp-1.0

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/%{name}

%changelog
* Fri Dec  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.7.1-1
- Update to 0.7.1

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.7.0-2
- Remove unneeded libglade BR

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.7.0-1
- Update to 0.7.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.6.4-3
- Move docs to noarch subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Peter Robinson <pbrobinson@gmail.com> 0.6.4-1
- New upstream release

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.3-3
- Add gtk-doc build req

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.3-2
- Fix summary

* Mon Oct 27 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.3-1
- New upstream version

* Sun Aug 31 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.2-1
- New upstream version

* Tue Aug 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.1-4
- Move glade files from devel to main rpm

* Tue Aug 12 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.1-3
- Patch to fix the build in rawhide

* Fri Aug 8 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.1-2
- Updates based on feedback

* Mon May 19 2008 Peter Robinson <pbrobinson@gmail.com> 0.6.1-1
- Initial package 
