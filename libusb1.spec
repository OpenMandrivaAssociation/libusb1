%define major 1
%define libname %mklibname usb %major
%define devellibname %mklibname -d usb %major
%define sdevellibname %mklibname -s -d usb %major

Summary: A library which allows userspace access to USB devices
Name: libusb1
Version: 1.0.2
Release: %mkrel 2
Source0: http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-
URL: http://libusb.wiki.sourceforge.net/Libusb1.0
BuildRequires: doxygen

%description
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

# fix build on both ia32 && ia64:
%ifarch x86_64
%package -n %libname
Summary: %summary
Group:	System/Libraries
Requires: pkgconfig

%description -n %libname
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.
%endif

%package -n %devellibname
Summary: Development files for libusb
Group:	Development/C
Requires: %{libname} = %{version}
Provides: libusb1-devel = %version, usb1-devel = %version
Requires: pkgconfig

%description -n %devellibname
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb1.

%package -n %sdevellibname
Summary: Static development files for libusb
Group:	Development/C
Requires: %devellibname = %{version}
Provides: usb1-static-devel = %version

%description -n %sdevellibname
This package contains static libraries to develop applications that use
libusb1.

%prep
%setup -q -n libusb-%{version}

%build
%configure
make CFLAGS="$RPM_OPT_FLAGS"
pushd doc
make docs
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS ChangeLog
%{_libdir}/*.so.*

%files -n %devellibname
%defattr(-,root,root)
%doc doc/html examples/*.c
%{_libdir}/pkgconfig/libusb-1.0.pc
%{_includedir}/*
%{_libdir}/*.so

%files -n %sdevellibname
%defattr(-,root,root)
%{_libdir}/*.a

