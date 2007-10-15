Summary:	Vector-based 2D animation software package
Summary(pl.UTF-8):	Pakiet oprogramowania do wektorowych animacji 2D
Name:		synfig
Version:	0.61.07
Release:	0.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/synfig/synfig-0.61.07.tar.gz
# Source0-md5:	c18c23abe8db6d856f39fe1617e05612
Patch0:		%{name}-openexr.patch
Patch1:	%{name}-noreconf.patch
Patch2:	%{name}-fix-stringh.patch
Patch3:	%{name}-crazy-debugging.patch
Patch4:	%{name}-includes.patch
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
. "config/build.cfg"

SED_SCRIPT="
s/@PACKAGE@/$PACKAGE/g;
s/@PACKAGE_NAME@/$PACKAGE_NAME/g;
s/@PACKAGE_BUGREPORT@/$PACKAGE_BUGREPORT/g;
s/@PACKAGE_TARNAME@/$PACKAGE_TARNAME/g;
s/@PACKAGE_VERSION@/$PACKAGE_VERSION/g;
s|@SVN_REPOSITORY@|$SVN_REPOSITORY|g;
s/@VERSION@/$VERSION/g;
s/@API_VERSION@/$API_VERSION/g;
s/@VERSION_MAJ@/$VERSION_MAJ/g;
s/@VERSION_MIN@/$VERSION_MIN/g;
s/@VERSION_REV@/$VERSION_REV/g;
s/@VERSION_REL@/$VERSION_REL/g;
s/@CFLAGS@//g;
"

for FILENAME in doxygen.cfg pkgconfig.pc; do 
	sed "$SED_SCRIPT" < "config/$FILENAME.in" > $FILENAME;
done

mv pkgconfig.pc "$PACKAGE_TARNAME.pc.in"

sed "$SED_SCRIPT" < "config/configure.ac" > configure.ac

%{__libtoolize} --ltdl
%{__aclocal} -I config
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/synfig*
%attr(755,root,root) %{_libdir}/libsynfig.so.*.*.*
%dir %{_libdir}/synfig
%dir %{_libdir}/synfig/modules
%attr(755,root,root) %{_libdir}/synfig/modules/*.so.*
%{_libdir}/synfig/modules/*.la
# XXX: %config() ???
%{_sysconfdir}/synfig_modules.cfg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsynfig.so
%{_libdir}/libsynfig.la
%{_includedir}/synfig-0.0
%{_pkgconfigdir}/synfig.pc
