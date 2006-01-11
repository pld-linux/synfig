#
Summary:	Vector-based 2D animation software package
Name:		synfig
Version:	0.61.03
Release:	0.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.bridgetone.com/voria/files/%{name}-%{version}.tar.gz
# Source0-md5:	79833d8a264fce9a891683bf8fb4a0a1
Patch0:		synfig-openexr.patch
URL:		http://www.synfig.com
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
/etc/synfig_modules.cfg
%attr(755,root,root) %{_bindir}/synfig*
/usr/include/synfig-0.0/synfig/*
%{_libdir}/libsynfig.la
%{_libdir}/libsynfig.so.0.0.0
%{_pkgconfigdir}/synfig.pc
%{_libdir}/synfig/modules/*.la
%{_libdir}/synfig/modules/*.so.*
