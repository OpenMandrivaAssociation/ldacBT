%define libname %mklibname ldac %{major}
%define develname %mklibname ldac -d

%define major 2

Name:           ldacBT
Version:        2.0.2.3
Release:        1
Summary:        A lossy audio codec for Bluetooth connections
License:        Apache-2.0
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/EHfive/ldacBT
Source0:        https://github.com/EHfive/ldacBT/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libname}
Summary:        A lossy audio codec for Bluetooth connections
Group:          System/Libraries

%description -n %{libname}
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%prep
%autosetup -n %{name} -p1

%build
%cmake \
	-DBUILD_STATIC_LIBS=OFF \
	-DLDAC_SOFT_FLOAT=OFF \
	-DINSTALL_LIBDIR=%{_libdir}
%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE
%{_libdir}/libldacBT_abr.so.*
%{_libdir}/libldacBT_enc.so.*

%files -n %{develname}
%dir %{_includedir}/ldac
%{_includedir}/ldac/ldacBT_abr.h
%{_includedir}/ldac/ldacBT.h
%{_libdir}/pkgconfig/ldacBT-abr.pc
%{_libdir}/pkgconfig/ldacBT-enc.pc
%{_libdir}/libldacBT_abr.so
%{_libdir}/libldacBT_enc.so
