#
# Conditional build:
%bcond_without	vala	# Vala API
#
Summary:	Unicode character map
Summary(pl.UTF-8):	Mapa znaków unikodowych
Name:		gucharmap
Version:	3.6.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gucharmap/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	a0e0cdf05a0db8a66b2da35b4f8b7f6e
URL:		http://live.gnome.org/Gucharmap
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-doc-utils >= 0.12.2
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18}
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,preun):	glib2 >= 1:2.32.0
Requires:	%{name}-libs = %{version}-%{release}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl.UTF-8
Gucharmap jest wartościową mapą znaków unikodowych.

%package libs
Summary:	gucharmap library for GTK+ 3
Summary(pl.UTF-8):	Biblioteka gucharmap dla GTK+ 3
Group:		X11/Libraries
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.0
Requires:	pango >= 1:1.20.0

%description libs
This package contains gucharmap library for GTK+ 3.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gucharmap dla GTK+ 3.

%package devel
Summary:	Headers for gucharmap (GTK+ 3 verson)
Summary(pl.UTF-8):	Pliki nagłówkowe gucharmap (wersja dla GTK+ 3)
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gtk+3-devel >= 3.4.0

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap. This version is targeted for GTK+ 3.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających gucharmap. Ta wersja jest przeznaczona dla GTK+ 3.

%package static
Summary:	Static gucharmap library for GTK+ 3
Summary(pl.UTF-8):	Statyczna biblioteka gucharmap dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap library for GTK+ 3.

%description static -l pl.UTF-8
Statyczna wersja biblioteki gucharmap dla GTK+ 3.

%package apidocs
Summary:	gucharmap library API documentation (GTK+ 3 version)
Summary(pl.UTF-8):	Dokumentacja API biblioteki gucharmap (wersja dla GTK+ 3)
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gucharmap library API documentation (GTK+ 3 version).

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gucharmap (wersja dla GTK+ 3).

%package -n vala-gucharmap
Summary:	gucharmap API for Vala language
Summary(pl.UTF-8):	API gucharmap dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.16

%description -n vala-gucharmap
gucharmap API for Vala language.

%description -n vala-gucharmap -l pl.UTF-8
API gucharmap dla języka Vala.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-introspection \
	--enable-static \
	%{?with_vala:--enable-vala} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	vapidir=%{_datadir}/vala/vapi

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING.UNICODE ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/charmap
%attr(755,root,root) %{_bindir}/gucharmap
%attr(755,root,root) %{_bindir}/gnome-character-map
%{_desktopdir}/gucharmap.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.gschema.xml

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

%if %{with vala}
%files -n vala-gucharmap
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/Gucharmap-2.90.vapi
%endif
