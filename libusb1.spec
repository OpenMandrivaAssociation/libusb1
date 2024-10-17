%define api 1.0
%define major 0
%define libname %mklibname usb %{api} %{major}
%define devellibname %mklibname -d usb %{api}
%define sdevellibname %mklibname -s -d usb %{api}

Summary:	A library which allows userspace access to USB devices
Name:		libusb1
Version:	1.0.9
Release:	ZED'S DEAD_BABY
License:	LGPLv2+
Group:		System/Libraries
URL:		https://libusb.wiki.sourceforge.net/Libusb1.0
Source0:	http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2
BuildRequires:	doxygen

%description
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package -n %{libname}
Summary:	A library which allows userspace access to USB devices
Group:		System/Libraries
# Package had originally wrong major:
Obsoletes:	%{_lib}usb1 < 1.0.3-2

%description -n %{libname}
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package -n %{devellibname}
Summary:	Development files for libusb
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libusb1-devel = %{version}-%{release}
Provides:	usb1-devel = %{version}-%{release}
Provides:	usb%{api}-devel = %{version}-%{release}
# Package had originally wrong api in name:
Obsoletes:	%{_lib}usb1-devel < 1.0.3-2

%description -n %{devellibname}
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb-1.0.

%package -n %{sdevellibname}
Summary:	Static development files for libusb
Group:		Development/C
Requires:	%{devellibname} = %{version}-%{release}
Provides:	usb1-static-devel = %{version}-%{release}
Provides:	usb%{api}-static-devel = %{version}-%{release}
# Package had originally wrong api in name:
Obsoletes:	%{_lib}usb1-static-devel < 1.0.3-2

%description -n %{sdevellibname}
This package contains static libraries to develop applications that use
libusb-1.0.

%prep
%setup -q -n libusb-%{version}

%build
# libusb-compat is in /lib and uses libusb1
%configure2_5x \
		--libdir=/%{_lib}

%make
pushd doc
make docs
popd

%install
%makeinstall_std

# static library is not needed in /lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/libusb-%{api}.a %{buildroot}%{_libdir}
# add a symlink just in case libtool expects it to be there due to it
# being referenced in the .la file
ln -s %{_libdir}/libusb-%{api}.a %{buildroot}/%{_lib}/libusb-%{api}.a
# move .pc file back
mv %{buildroot}/%{_lib}/pkgconfig %{buildroot}%{_libdir}

%files -n %{libname}
/%{_lib}/libusb*-%{api}.so.%{major}*

%files -n %{devellibname}
%doc AUTHORS COPYING README NEWS ChangeLog
%doc doc/html examples/*.c
%{_libdir}/pkgconfig/libusb-%{api}.pc
%{_includedir}/libusb-%{api}
/%{_lib}/libusb-%{api}.so

%files -n %{sdevellibname}
/%{_lib}/libusb-%{api}.*a
%{_libdir}/libusb-%{api}.a

%changelog
* Mon Apr 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.9-1mdv2012.0
+ Revision: 792783
- version update 1.0.9

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-2
+ Revision: 660291
- mass rebuild

* Mon Aug 02 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 565042
- New version 1.0.8

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0.7-3mdv2010.1
+ Revision: 540038
- rebuild so that shared libraries are properly stripped again

* Sun Apr 25 2010 Anssi Hannula <anssi@mandriva.org> 1.0.7-2mdv2010.1
+ Revision: 538655
- rebuild due to missing library subpkg on x86_64

* Sun Apr 25 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.7-1mdv2010.1
+ Revision: 538645
- New version 1.0.7
- New version 1.0.7

* Wed Dec 02 2009 Thierry Vignaud <tv@mandriva.org> 1.0.6-1mdv2010.1
+ Revision: 472679
- new release

* Tue Nov 17 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.5-1mdv2010.1
+ Revision: 466840
- 1.0.5 release

* Fri Sep 18 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-3mdv2010.0
+ Revision: 444270
- remove explicit Requires: on pkgconfig, it's added automatically when needed

* Fri Sep 11 2009 Anssi Hannula <anssi@mandriva.org> 1.0.3-2mdv2010.0
+ Revision: 438531
- move library to /lib as it is used by libusb-compat which is also there
- fix library naming (major and api were wrong)
- ensure major and api correctness in file list

* Fri Sep 04 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-1mdv2010.0
+ Revision: 430540
- new upstream release
- package .la files static libraries
- use %%configure2_5x, %%make and %%makeinstall_std

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2010.0
+ Revision: 428705
- fix requires on x86_64
- do not call ldconfig (already done by rpm)

* Thu Aug 13 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 416051
- import libusb1

