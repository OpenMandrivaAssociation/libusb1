
%define api 1.0
%define major 0
%define libname %mklibname usb %api %major
%define devellibname %mklibname -d usb %api
%define sdevellibname %mklibname -s -d usb %api

Summary: A library which allows userspace access to USB devices
Name: libusb1
Version: 1.0.3
Release: %mkrel 3
Source0: http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-
URL: http://libusb.wiki.sourceforge.net/Libusb1.0
BuildRequires: doxygen

%description
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package -n %libname
Summary: %summary
Group:	System/Libraries
# Package had originally wrong major:
Obsoletes: %{_lib}usb1 < 1.0.3-2

%description -n %libname
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package -n %devellibname
Summary: Development files for libusb
Group:	Development/C
Requires: %{libname} = %{version}
Provides: libusb1-devel = %version, usb1-devel = %version, usb%{api}-devel = %version
# Package had originally wrong api in name:
Obsoletes: %{_lib}usb1-devel < 1.0.3-2

%description -n %devellibname
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb-1.0.

%package -n %sdevellibname
Summary: Static development files for libusb
Group:	Development/C
Requires: %devellibname = %{version}
Provides: usb1-static-devel = %version, usb%{api}-static-devel
# Package had originally wrong api in name:
Obsoletes: %{_lib}usb1-static-devel < 1.0.3-2

%description -n %sdevellibname
This package contains static libraries to develop applications that use
libusb-1.0.

%prep
%setup -q -n libusb-%{version}

%build
# libusb-compat is in /lib and uses libusb1
%configure2_5x --libdir=/%{_lib}
%make
pushd doc
make docs
popd

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# static library is not needed in /lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/libusb-%api.a %{buildroot}%{_libdir}
# add a symlink just in case libtool expects it to be there due to it
# being referenced in the .la file
ln -s %{_libdir}/libusb-%api.a %{buildroot}/%{_lib}/libusb-%api.a
# move .pc file back
mv %{buildroot}/%{_lib}/pkgconfig %{buildroot}%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS ChangeLog
/%{_lib}/libusb*-%{api}.so.%{major}*

%files -n %devellibname
%defattr(-,root,root)
%doc doc/html examples/*.c
%{_libdir}/pkgconfig/libusb-%api.pc
%{_includedir}/libusb-%api
/%{_lib}/libusb-%api.so

%files -n %sdevellibname
%defattr(-,root,root)
/%{_lib}/libusb-%api.*a
%{_libdir}/libusb-%api.a

