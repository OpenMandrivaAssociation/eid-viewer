%define Werror_cflags %nil
%define debug_package %{nil}

Name:           eid-viewer
Version:        4.1.16
Release:        1
Summary:        The eID Middleware offers components for using the Belgian eID
License:        LGPLv3
Group:          Networking/Other
URL:            http://github.com/Fedict/eid-mw2
Source0:        https://dist.eid.belgium.be/continuous/sources/%{name}-%{version}-v%{version}.src.tar.gz
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Software that support electronic person identification for Belgian eID.

%prep
%setup -qn %{name}-%{version}
%apply_patches

%build
%configure2_5x \
	--with-qt --disable-static

%make

%install
%makeinstall_std

%files

%doc COPYING README NEWS
%{_bindir}/eid-viewer
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/%{name}.png
