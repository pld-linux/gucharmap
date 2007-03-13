Summary:	Unicode character map
Summary(pl.UTF-8):	Mapa znaków unikodowych
Name:		gucharmap
Version:	1.10.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gucharmap/1.10/%{name}-%{version}.tar.bz2
# Source0-md5:	a0e01bcff2bc5e35ec88f60a383051d3
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.10.1
BuildRequires:	gtk+2-devel >= 2:2.10.10
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libgnomeui-devel >= 2.18.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl.UTF-8
Gucharmap jest wartościową mapą znaków unikodowych.

%package libs
Summary:	gucharmap library
Summary(pl.UTF-8):	Biblioteka gucharmap
Group:		Development/Libraries
Requires:	libgnomeui >= 2.18.0
Requires:	pango >= 1:1.16.1

%description libs
This package contains gucharmap library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gucharmap.

%package devel
Summary:	Headers for gucharmap
Summary(pl.UTF-8):	Pliki nagłówkowe gucharmap
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.10
Requires:	libgnomeui-devel >= 2.18.0
Requires:	pango-devel >= 1:1.16.1

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających gucharmap.

%package static
Summary:	Static gucharmap libraries
Summary(pl.UTF-8):	Statyczne biblioteki gucharmap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek gucharmap.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_prepare}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf gucharmap $RPM_BUILD_ROOT%{_bindir}/charmap

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*charmap
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_omf_dest_dir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
