Summary:	Unicode character map
Summary(pl):	Mapa znak�w unikodowych
Name:		gucharmap
Version:	1.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gucharmap/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	a75cc3dcc9fb3d2edecc4da936e80e3a
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.10.3
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.14.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2 >= 2:2.10.3
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl
Gucharmap jest warto�ciow� map� znak�w unikodowych.

%package libs
Summary:	gucharmap library
Summary(pl):	Biblioteka gucharmap
Group:		Development/Libraries
Requires:	libgnomeui >= 2.16.0
Requires:	pango >= 1:1.14.3

%description libs
This package contains gucharmap library.

%description libs -l pl
Pakiet ten zawiera bibliotek� gucharmap.

%package devel
Summary:	Headers for gucharmap
Summary(pl):	Pliki nag��wkowe gucharmap
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.3
Requires:	libgnomeui-devel >= 2.16.0
Requires:	pango-devel >= 1:1.14.3

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilacji program�w
u�ywaj�cych gucharmap.

%package static
Summary:	Static gucharmap libraries
Summary(pl):	Statyczne biblioteki gucharmap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap libraries.

%description static -l pl
Statyczna wersja bibliotek gucharmap.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_prepare}
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
%{_desktopdir}/*
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
