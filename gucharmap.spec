Summary:	Unicode character map
Summary(pl.UTF-8):	Mapa znaków unikodowych
Name:		gucharmap
Version:	3.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gucharmap/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	161f1ce0ca6550036eb86f22f7ac585a
URL:		http://live.gnome.org/Gucharmap
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.12.2
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl.UTF-8
Gucharmap jest wartościową mapą znaków unikodowych.

%package libs
Summary:	gucharmap library
Summary(pl.UTF-8):	Biblioteka gucharmap
Group:		X11/Libraries
Requires:	pango >= 1:1.20.0

%description libs
This package contains gucharmap library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gucharmap.

%package devel
Summary:	Headers for gucharmap
Summary(pl.UTF-8):	Pliki nagłówkowe gucharmap
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2-devel >= 2.24.0
Requires:	gtk+3-devel >= 3.0.0

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających gucharmap.

%package static
Summary:	Static gucharmap libraries
Summary(pl.UTF-8):	Statyczne biblioteki gucharmap
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek gucharmap.

%package apidocs
Summary:	gucharmap library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gucharmap
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gucharmap library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gucharmap.

%package -n gucharmap2-libs
Summary:	gucharmap library
Summary(pl.UTF-8):	Biblioteka gucharmap
Group:		X11/Libraries
Requires:	pango >= 1:1.20.0

%description -n gucharmap2-libs
This package contains gucharmap library.

%description -n gucharmap2-libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gucharmap.

%package -n gucharmap2-devel
Summary:	Headers for gucharmap
Summary(pl.UTF-8):	Pliki nagłówkowe gucharmap
Group:		X11/Development/Libraries
Requires:	gucharmap2-libs = %{version}-%{release}
Requires:	GConf2-devel >= 2.24.0
Requires:	gtk+2-devel >= 2:2.18.0

%description -n gucharmap2-devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap.

%description -n gucharmap2-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających gucharmap.

%package -n gucharmap2-static
Summary:	Static gucharmap libraries
Summary(pl.UTF-8):	Statyczne biblioteki gucharmap
Group:		X11/Development/Libraries
Requires:	gucharmap2-devel = %{version}-%{release}

%description -n gucharmap2-static
Static version of gucharmap libraries.

%description -n gucharmap2-static -l pl.UTF-8
Statyczna wersja bibliotek gucharmap.

%package -n gucharmap2-apidocs
Summary:	gucharmap library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gucharmap
Group:		Documentation
Requires:	gtk-doc-common

%description -n gucharmap2-apidocs
gucharmap library API documentation.

%description -n gucharmap2-apidocs -l pl.UTF-8
Dokumentacja API biblioteki gucharmap.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
COMMON_ARGS="--disable-silent-rules \
	--disable-scrollkeeper \
	--enable-introspection \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--enable-static"
mkdir gtk{2,3}
cd gtk2
../%configure \
	--with-gtk=2.0 \
	$COMMON_ARGS
%{__make}
cd ../gtk3
../%configure \
	--with-gtk=3.0 \
	$COMMON_ARGS
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

cd gtk2
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../gtk3
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gucharmap.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gucharmap.schemas

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n gucharmap2-libs -p /sbin/ldconfig
%postun	-n gucharmap2-libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/charmap
%attr(755,root,root) %{_bindir}/gucharmap
%attr(755,root,root) %{_bindir}/gnome-character-map
%{_sysconfdir}/gconf/schemas/gucharmap.schemas
%{_desktopdir}/gucharmap.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap_2_90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgucharmap_2_90.so.7
%{_libdir}/girepository-1.0/Gucharmap-2.90.typelib


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap_2_90.so
%{_includedir}/gucharmap-2.90
%{_pkgconfigdir}/gucharmap-2.90.pc
%{_datadir}/gir-1.0/Gucharmap-2.90.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgucharmap_2_90.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gucharmap-2.90

%files -n gucharmap2-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgucharmap.so.7
%{_libdir}/girepository-1.0/Gucharmap-2.0.typelib

%files -n gucharmap2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap.so
%{_includedir}/gucharmap-2.0
%{_pkgconfigdir}/gucharmap-2.pc
%{_datadir}/gir-1.0/Gucharmap-2.0.gir

%files -n gucharmap2-static
%defattr(644,root,root,755)
%{_libdir}/libgucharmap.a

%files -n gucharmap2-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gucharmap-2.0
