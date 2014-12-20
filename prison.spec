%define major 1
%define libname %mklibname KF5Prison %{major}
%define devname %mklibname KF5Prison -d
%define git 20141220

Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison
Group:		Development/C++
Version:	1.2.0
Release:	%{?git:0.%{git}.}1
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
%if %git
# git://anongit.kde.org/prison
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	ftp://ftp.kde.org/pub/kde/stable/prison/1.1/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	extra-cmake-modules5
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	qt5-devel

%description
Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%package -n %{libname}
Summary:	Prison library
Group:		System/Libraries

%description -n %{libname}
Library for %{name}.

Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%files -n %{libname}
%{_libdir}/libKF5Prison.so.%{major}*

%package -n %{devname}
Summary:	Prison development files
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for applications that use %{name}.

%files -n %{devname}
%doc LICENSE
%{_includedir}/KF5/PRISON
%{_includedir}/KF5/prison_version.h
%{_libdir}/cmake/KF5Prison
%{_libdir}/libKF5Prison.so
%{_libdir}/qt5/mkspecs/modules/*.pri

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install