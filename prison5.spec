%define major 1
%define libname %mklibname KF5Prison %{major}
%define devname %mklibname KF5Prison -d
%define git 20161024
%define pname prison

Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison5
Group:		Development/C++
Version:	1.2.1
Release:	%{?git:0.%{git}.}4
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
%if %git
# git clone git://anongit.kde.org/prison -b frameworks
# git archive --format=tar --prefix prison-1.2.1-$(date +%Y%m%d)/ HEAD | xz -vf > prison-1.2.1-$(date +%Y%m%d).tar.xz
Source0:	%{pname}-%{version}-%{git}.tar.xz
%else
Source0:	http://download.kde.org/stable/prison/1.1/src/%{pname}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)

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
Provides:	%{pname}-devel = %{EVRD}

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
%setup -qn %{pname}-%{version}-%{git}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
