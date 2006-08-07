Summary:	Vector-based 2D animation software package
Summary(pl):	Pakiet oprogramowania do wektorowych animacji 2D
Name:		synfig
Version:	0.61.03
Release:	0.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.bridgetone.com/voria/files/%{name}-%{version}.tar.gz
# Source0-md5:	79833d8a264fce9a891683bf8fb4a0a1
Patch0:		%{name}-openexr.patch
URL:		http://www.synfig.com/
BuildRequires:	ETL
BuildRequires:	libxml++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synfig is a powerful, industrial-strength vector-based 2D animation 
software package, designed from the ground-up for producing 
feature-film quality animation with fewer people and resources. 
While there are many other programs currently on the market to aid 
with the efficient production of 2D animation, we are currently 
unaware of any other software that can do what our software can.

%description -l pl
Synfig to potê¿ny, o sile przemys³owej pakiet oprogramowania do
wektorowych animacji 2D, zaprojektowany od podstaw do tworzenia
animacji o jako¶ci filmowej przy mniejszym zaanga¿owaniu ludzi i
zasobów. O ile na rynku jest wiele innych programów pomagaj±cych przy
wydajnej produkcji animacji 2D, autorzy nie znaj± innego
oprogramowania o takich mo¿liwo¶ciach jak synfig.

%prep
%setup -q
%patch0 -p0
cp config/* .

%build
export PACKAGE_TARNAME=synfig
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/synfig*
%attr(755,root,root) %{_libdir}/libsynfig.so.*.*.*
%dir %{_libdir}/synfig
%dir %{_libdir}/synfig/modules
%attr(755,root,root) %{_libdir}/synfig/modules/*.so.*
%{_libdir}/synfig/modules/*.la
/etc/synfig_modules.cfg

#%files devel
#%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsynfig.so
%{_libdir}/libsynfig.la
%{_includedir}/synfig-0.0
%{_pkgconfigdir}/synfig.pc
