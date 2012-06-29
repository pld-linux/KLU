Summary:	KLU: sparse LU factorization, for circuit simulation
Summary(pl.UTF-8):	KLU - rzadki rozkład LU na potrzeby symulacji obwodów
Name:		KLU
Version:	1.2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/klu/%{name}-%{version}.tar.gz
# Source0-md5:	e656523b71364e17b3b9e7ba3fc3981b
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/klu/
BuildRequires:	AMD-devel >= 2.3.0
BuildRequires:	BTF-devel >= 1.2.0
BuildRequires:	COLAMD-devel >= 2.8.0
BuildRequires:	SuiteSparse_config >= 4.0.0
BuildRequires:	libtool >= 2:1.5
Requires:	AMD >= 2.3.0
Requires:	BTF >= 1.2.0
Requires:	COLAMD >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KLU is a sparse LU factorization algorithm well-suited for use in
circuit simulation.

%description -l pl.UTF-8
KLU to algorytm rozkładu LU macierzy rzadkich dobrze pasujący do
zastosowań w symulacji obwodów.

%package devel
Summary:	Header files for KLU library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki KLU
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	AMD-devel >= 2.3.0
Requires:	BTF-devel >= 1.2.0
Requires:	COLAMD-devel >= 2.8.0
Requires:	SuiteSparse_config >= 4.0.0

%description devel
Header files for KLU library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki KLU.

%package static
Summary:	Static KLU library
Summary(pl.UTF-8):	Statyczna biblioteka KLU
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static KLU library.

%description static -l pl.UTF-8
Statyczna biblioteka KLU.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/klu

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/klu

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libklu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libklu.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/{KLU_UserGuide,palamadai_e}.pdf
%attr(755,root,root) %{_libdir}/libklu.so
%{_libdir}/libklu.la
%{_includedir}/klu

%files static
%defattr(644,root,root,755)
%{_libdir}/libklu.a
