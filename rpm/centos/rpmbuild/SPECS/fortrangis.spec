Summary: FortranGIS Fortran interfaces Open Source GIS libraries 
Name: fortrangis
Version: 2.4
Release: 2
License: LGPL
Group: Applications/GIS
URL: http://fortrangis.berlios.de/
Packager: Davide Cesari <dcesari69@gmail.com>
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
BuildRequires: shapelib-devel gdal-devel proj-devel gcc-gfortran libtool

%if 0%{?fedora} < 9 || 0%{?rhel}
%define _fmoddir       %{_libdir}/gfortran/modules
%endif

%package -n fortrangis-devel
Summary:  FortranGIS development files
Group: Applications/GIS
Requires: %{name}

%if 0%{?fedora} >= 9
%package -n fortrangis-doc
Summary:  FortranGIS documentation
Group: Applications/GIS
%endif

%description -n fortrangis-devel
Development files, necessary for building applications using
FortranGIS

%if 0%{?fedora} >= 9
%description -n fortrangis-doc
Doxygen documentation for FortranGIS package
%endif

%description
FortranGIS is a collection of Fortran interfaces to the most common
Open Source GIS libraries, plus some more Fortran-specific tools.

The libraries interfaced at the moment are Shapelib, GDAL and Proj.

%prep
%setup -q

%build
%configure %{?fedora:CPPFLAGS=-I/usr/include/libshp} %{?rhel:--disable-doxydoc}
make 

%install
make DESTDIR=%{buildroot} install
%if 0%{?fedora} >= 9  || 0%{?rhel}
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}
mv $RPM_BUILD_ROOT%{_includedir}/*.mod $RPM_BUILD_ROOT%{_fmoddir}
%endif

%files
%defattr(-, root, root)
%{_libdir}/*.so.*
%doc %{_datadir}/doc/%{name}-%{version}/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/README

%files -n fortrangis-devel
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%if 0%{?fedora} < 9  && !0%{?rhel}
%{_includedir}/*
%else
%{_fmoddir}/*.mod
%endif

%if 0%{?fedora} >= 9
%files -n fortrangis-doc
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/html
%endif

%clean
rm -rf %{buildroot}

%pre

%post

%preun

%postun

%changelog
* Tue Mar 22 2016 Dario Mastropasqua,,, <dariomas@users.noreply.github.com> 2.4-2
- disabled fortrangis-doc package in RHEL (CentOS) because doxygen crashes
- corrected Fortran mod dir for RHEL (CentOS)
