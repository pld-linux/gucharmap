Summary:	Unicode character map
Summary(pl.UTF-8):	Mapa znaków unikodowych
Name:		gucharmap
Version:	2.24.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gucharmap/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	7e02c06f3b8d375e059073af378bf093
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.12.2
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
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
Requires:	gtk+2-devel >= 2:2.14.0

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
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/charmap
%attr(755,root,root) %{_bindir}/gucharmap
%attr(755,root,root) %{_bindir}/gnome-character-map
%{_sysconfdir}/gconf/schemas/gucharmap.schemas
%{_desktopdir}/gucharmap.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgucharmap.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap.so
%{_libdir}/libgucharmap.la
%{_includedir}/gucharmap-2
%{_pkgconfigdir}/gucharmap-2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgucharmap.a
