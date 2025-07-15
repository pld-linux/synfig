Summary:	Vector-based 2D animation software package
Summary(pl.UTF-8):	Pakiet oprogramowania do wektorowych animacji 2D
Name:		synfig
Version:	0.64.2
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6ac9536e4d0a584d57e64a8eca38e6c3
Patch0:		%{name}-m4.patch
URL:		http://www.synfig.org/
BuildRequires:	ETL >= 0.04.17
BuildRequires:	boost-devel >= 1.32.0
BuildRequires:	libxml++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synfig is a powerful, industrial-strength vector-based 2D animation 
software package, designed from the ground-up for producing 
feature-film quality animation with fewer people and resources. 
While there are many other programs currently on the market to aid 
with the efficient production of 2D animation, we are currently 
unaware of any other software that can do what our software can.

%description -l pl.UTF-8
Synfig to potężny, o sile przemysłowej pakiet oprogramowania do
wektorowych animacji 2D, zaprojektowany od podstaw do tworzenia
animacji o jakości filmowej przy mniejszym zaangażowaniu ludzi i
zasobów. O ile na rynku jest wiele innych programów pomagających przy
wydajnej produkcji animacji 2D, autorzy nie znają innego
oprogramowania o takich możliwościach jak synfig.

%package devel
Summary:	Header files for Synfig
Summary(pl.UTF-8):	Pliki nagłówkowe Synfiga
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Synfig.

%description devel -l pl.UTF-8
Pliki nagłówkowe Synfiga.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/synfig*
%attr(755,root,root) %{_libdir}/libsynfig.so.*.*.*
%dir %{_libdir}/synfig
%dir %{_libdir}/synfig/modules
%attr(755,root,root) %{_libdir}/synfig/modules/*.so
%{_libdir}/synfig/modules/*.la
# XXX: %config() ???
%{_sysconfdir}/synfig_modules.cfg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsynfig.so
%{_libdir}/libsynfig.la
%{_includedir}/synfig-0.0
%{_pkgconfigdir}/synfig.pc
